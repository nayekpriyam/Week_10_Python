class SimpleTextEditor:
    def __init__(self):
        self.text = []  
        self.ops = []   

    def append(self, w: str):
        self.text.extend(w)
        self.ops.append(('del', len(w)))

    def delete(self, k: int):
        k = min(k, len(self.text))
        removed = ''.join(self.text[-k:])
        del self.text[-k:]
        self.ops.append(('add', removed))

    def print_k(self, k: int):
        if 1 <= k <= len(self.text):
            print(self.text[k-1])
        else:
            print('')  

    def undo(self):
        if not self.ops:
            return
        op, val = self.ops.pop()
        if op == 'del':
            del self.text[-val:]
        elif op == 'add':
            self.text.extend(val)

def process_commands(commands):
    editor = SimpleTextEditor()
    for cmd in commands:
        parts = cmd.split()
        t = parts[0]
        if t == '1': 
            editor.append(parts[1])
        elif t == '2':  
            editor.delete(int(parts[1]))
        elif t == '3':  
            editor.print_k(int(parts[1]))
        elif t == '4':  
            editor.undo()
