import tkinter as tk
from tkinter import ttk, messagebox
import json
import time
import threading
import random
import alpaca_trade_api as tradeapi
import openai

DATA_FILE = "equities.json"

key="SUA_ALPACA_KEY"
secret_key="SUA_ALPACA_SECRET"
BASE_URL = "https://paper-api.alpaca.markets"

openai.api_key = "SUA_CHAVE_OPENAI"


def fetch_portfolio():
    positions = api.list_positions()
    portfolio = []
    for pos in positions:
      portfolio.append({
          'symbol': pos.symbol,
          'qty': pos.qty,
          'entry_price': pos.avg_entry_price,
          'current_price': pos.current_price,
          'unrealized_pl': pos.unrealized_pl,
          'ide': 'buy'
      })
    return portfolio

def fetch_open_orders():
    orders = api.list_orders(status='open')
    open_orders = []
    for order in orders:
        open_orders.append({
            'symbol': order.symbol,
            'qty': order.qty,
            'side': 'buy',
            'limit_price': order.limit_price,
        })
    return open_orders

def fetch_mock_api(symbol):
    return {
        "price" : 100
    }


def chatgpt_response(message):
    portfolio_data = fetch_portfolio()
    open_orders = fetch_open_orders()

    pre_prompt = f"""
    You are an AI Portfolio Manager responsible for analyzing my portfolio.

    Here is my portfolio: {portfolio_data}

    Here are my open orders {open_orders}

    Overall, answer the following question: {message}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"system", "content":pre_prompt}],
        api_key = "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"
    )
    return response['choices'][0]['message']['content']


class TradingBotGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Trading Bot")
        self.equities = self.load_equities()
        self.system_running = False

        self.form_frame = tk.Frame(root)
        self.form_frame.pack(pady=10)

        # Form to add a new equity to our trading bot
        tk.Label(self.form_frame, text="Symbol:").grid(row=0, column=0)
        self.symbol_entry = tk.Entry(self.form_frame)
        self.symbol_entry.grid(row=0, column=1)

        #tk.Label(self.form_frame, text="Levels:").grid(row=0, column=2)
        #self.levels_entry = tk.Entry(self.form_frame)
        #self.levels_entry.grid(row=0, column=3)

        #tk.Label(self.form_frame, text="Drawdown%:").grid(row=0, column=4)
        ##self.drawdown_entry = tk.Entry(self.form_frame)
        #self.drawdown_entry.grid(row=0, column=5)

        self.add_button = tk.Button(self.form_frame, text="Add Equity", command=self.add_equity)
        self.add_button.grid(row=0, column=6)


        # Table to track the traded equities
        self.tree = ttk.Treeview(root, columns=("Symbol", "Position", "Entry Price", "Current Price", "Stop Loss", "Take Profit", "Status"), show='headings')
        for col in ["Symbol", "Position", "Entry Price", "Current Price", "Stop Loss", "Take Profit", "Status"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10)

        # Buttons to control the bot
        self.toggle_system_button = tk.Button(root, text="Toggle Selected System", command=self.toggle_selected_system)
        self.toggle_system_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Selected Equity", command=self.remove_selected_equity)
        self.remove_button.pack(pady=5)

         # AI Component
        self.chat_frame = tk.Frame(root)
        self.chat_frame.pack(pady=10)

        self.chat_input = tk.Entry(self.chat_frame, width=50)
        self.chat_input.grid(row=0, column=0, padx=5)

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1)

        self.chat_output = tk.Text(root, height=5, width=60, state=tk.DISABLED)
        self.chat_output.pack()

        # Load saved data
        self.refresh_table()

        # Auto-refreshing
        self.auto_update()  # inicia o loop de atualização
        #self.running = True
        #self.auto_update_thread = threading.Thread(target=self.auto_update, daemon=True)
        #self.auto_update_thread.start()

    
    def add_equity(self):
        symbol = self.symbol_entry.get().upper()

        if not symbol:
            messagebox.showerror("Error", "Invalid Symbol")
            return
        
        try:
            asset = api.get_asset(symbol)
            if not asset.tradable:
                messagebox.showerror("Erro de Ativo", f"O ativo {symbol} existe, mas não é negociável.")
                return
        except tradeapi.rest.APIError:
            messagebox.showerror("Erro de Ativo", f"O ativo com o ticker '{symbol}' não foi encontrado.")
            return

        self.equities[symbol] = {
            "position": 0,
            "entry_price": 0,
            "stop_loss": 0,
            "take_profit": 0,
            "status": "Off"
        }

        self.save_equities()
        self.refresh_table()


        
    def toggle_selected_system(self):
            selected_items = self.tree.selection()
            if not selected_items:
                messagebox.showwarning("Warning", "No Equity is Selected")
                return
            
            for item in selected_items:
                symbol = self.tree.item(item)['values'][0]
                self.equities[symbol]['status'] = "On" if self.equities[symbol]['status'] == "Off" else "Off"

            self.save_equities()
            self.refresh_table()


    def remove_selected_equity(self):
            selected_items = self.tree.selection()
            if not selected_items:
                messagebox.showwarning("Warning", "No Equity Selected")
                return
            
            for item in selected_items:
                symbol = self.tree.item(item)['values'][0]
                if symbol in self.equities:
                    del self.equities[symbol]
            
            self.save_equities()
            self.refresh_table()

    def send_message(self):
            message = self.chat_input.get()
            if not message:
                return
            response = chatgpt_response(message)

            self.chat_output.config(state=tk.NORMAL)
            self.chat_output.insert(tk.END, f"You: {message}\n{response}\n\n")
            self.chat_output.config(state=tk.DISABLED)
            self.chat_input.delete(0, tk.END)

    def fetch_alpaca_data(self, symbol):
        try:
            barset = api.get_latest_trade(symbol)
            return {"price":barset.price}
        except Exception as e:
            return {"price":-1}

    def check_existing_orders(self, symbol, price):
        try:
            orders = api.list_orders(status='open', symbols=symbol)
            for order in orders:
                if float(order.limit_price) == price:
                    return True
        except Exception as e:
            messagebox.showerror("API Error", f"Error Checking Orders {e}")
        return False
    
    def get_max_entry_price(self, symbol):
        try:
            orders = api.list_orders(status="filled", limit=50)
            prices = [float(order.filled_avg_price) for order in orders if order.filled_avg_price and order.symbol == symbol]
            return max(prices) if prices else -1
        except Exception as e:
            messagebox.showerror("API Error", f"Error Fetching Orders {e}")
            return 0
    
    def trade_systems(self):
        for symbol, data in self.equities.items():
            if data['status'] == 'On':
                try:
                    # tenta obter posição atual
                    position = api.get_position(symbol)
                    qty = int(float(position.qty))  # quantidade em carteira
                    entry_price = float(position.avg_entry_price)
                    current_price = float(position.current_price)

                    # define limites
                    stop_loss_price = round(entry_price * 0.95, 2)   # -5%
                    take_profit_price = round(entry_price * 1.10, 2) # +10%

                    # 🔥 atualiza o dicionário do equity
                    self.equities[symbol]['position'] = qty
                    self.equities[symbol]['entry_price'] = entry_price
                    self.equities[symbol]['stop_loss'] = stop_loss_price
                    self.equities[symbol]['take_profit'] = take_profit_price
                    self.equities[symbol]['current_price'] = current_price


                    # regra de stop loss
                    if current_price <= stop_loss_price:
                        api.submit_order(
                            symbol=symbol,
                            qty=qty,
                            side="sell",
                            type="market",
                            time_in_force="gtc"
                        )
                        messagebox.showinfo("Stop Loss", f"Stop loss acionado em {symbol} @ {current_price}")
                        self.equities[symbol]['status'] = "Off"

                    # regra de take profit
                    elif current_price >= take_profit_price:
                        api.submit_order(
                            symbol=symbol,
                            qty=qty,
                            side="sell",
                            type="market",
                            time_in_force="gtc"
                        )
                        messagebox.showinfo("Take Profit", f"Take profit acionado em {symbol} @ {current_price}")
                        self.equities[symbol]['status'] = "Off"

                except tradeapi.rest.APIError:
                    # sem posição ainda → compra inicial
                    api.submit_order(
                        symbol=symbol,
                        qty=1,
                        side="buy",
                        type="market",
                        time_in_force="gtc"
                    )
                    messagebox.showinfo("Compra Inicial", f"Compra inicial realizada em {symbol}")
                    time.sleep(2)

        self.save_equities()
        self.refresh_table()


    def place_order(self, symbol, price, level):
        if -level in self.equities[symbol]['levels'] or '-1' in self.equities[symbol]['levels'].keys():
            return
        
        try:
            api.submit_order(
                symbol=symbol,
                qty=1,
                side='buy',
                type='limit',
                time_in_force='gtc',
                limit_price=price
            )
            self.equities[symbol]['levels'][-level] = price
            del self.equities[symbol]['levels'][level]
            print(f"Placed order for {symbol}@{price}")
        except Exception as e:
            messagebox.showerror("Order Error", f"Error placing order {e}")
            
    def refresh_table(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            for symbol, data in self.equities.items():
                self.tree.insert("", "end", values=(
                    symbol,
                    data['position'],
                    data['entry_price'],
                    data.get('current_price', ''),
                    data.get('stop_loss', ''),
                    data.get('take_profit', ''),
                    data['status']
                ))

    def auto_update(self):
            self.trade_systems()
            self.root.after(5000, self.auto_update)
            #while self.running:
            #    time.sleep(5)
            #    self.trade_systems()
    
    def save_equities(self):
            with open(DATA_FILE, 'w') as f:
                json.dump(self.equities, f)
    
    def load_equities(self):
            try:
                with open(DATA_FILE, 'r') as f:
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                return {}
            

    def on_close(self):
        self.running = False
        self.save_equities()
        self.root.destroy()
    
if __name__ == '__main__':
    root = tk.Tk()
    app = TradingBotGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()


