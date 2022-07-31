data = {
    'name': 'Ali',
    'national_code':'0410488683',
}

class ValidationName():
    def __init__(self, data):
        self.data = data
        self.key = 'name'

    def __call__(self, *args, **kwgs):
        target_name = self.data.get(self.key)
        print(True if target_name.isalpha() and len(target_name) >= 3 else False)

class ValidationCode():
    def __init__(self, data):
        self.data = data
        self.key = 'national_code'

    def __call__(self,  *args, **kwgs):
        target_code = self.data.get(self.key)
        print(True if target_code.isdigit() and target_code.startswith('0') and len(target_code)==10 else False)



validator_list = [ValidationName(data), ValidationCode(data)]
for validator in validator_list:
    validator()