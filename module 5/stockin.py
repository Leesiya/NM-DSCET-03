from flask import Flask, render_template, request

app = Flask(__name__)

inventory = {'item1': 10, 'item2': 20, 'item3': 15}  # Sample inventory data

@app.route('/', methods=['GET', 'POST'])
def stock_inventory():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = int(request.form['quantity'])
        action = request.form['action']

        if action == 'add':
            if item_name in inventory:
                inventory[item_name] += quantity
            else:
                inventory[item_name] = quantity
        elif action == 'remove':
            if item_name in inventory:
                if inventory[item_name] >= quantity:
                    inventory[item_name] -= quantity
                    if inventory[item_name] == 0:
                        del inventory[item_name]
                else:
                    return "Insufficient quantity in inventory."
            else:
                return "Item not found in inventory."

    return render_template('inventory.html', inventory=inventory)

if __name__ == '__main__':
    app.run(debug=True)