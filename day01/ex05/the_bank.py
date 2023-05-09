
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount


def check_account(account):
    # Get all attribute names
    attr_names = dir(account)

    # Check for even number of attributes
    # if len(attr_names) % 2 != 0:
    #     return False

    # Check for attribute starting with 'b'
    # if not any(attr.startswith('b') for attr in attr_names):
    #     return False
    # Check for attributes starting with 'zip' or 'addr'
    if any(attr.startswith('addr') for attr in attr_names):
        return False

    # Check for 'name', 'id', and 'value' attributes
    # if any(attr in ['name', 'id', 'value'] for attr in attr_names):
    #     return False

    # Check that 'name' attribute is a string
    if not isinstance(account.name, str):
        return False

    # Check that 'id' attribute is an integer
    if not isinstance(account.id, int):
        return False

    # Check that 'value' attribute is an int or a float
    if not isinstance(account.value, (int, float)):
        return False

    # If all checks pass, return True
    return True

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if not check_account(new_account):
            print("created fail ", new_account.name)
            return False
        else:
            print("created sucess ", new_account.name)
        self.accounts.append(new_account)
        return True            
    
    
    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None
    
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # ... Your code ...
        source = self.get_account(origin)
        receipter = self.get_account(dest)
                         
        if not all([check_account(source), check_account(receipter)]) :
            return False 
        if source.value < 0 or amount > source.value:
            return False
        if origin == dest:
            return True
        source.value -= amount
        receipter.value -= amount

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        if not self.get_account(name):
            return False
        
        return True
    
    # def print_compte_name(self):
    #     for x in self.accounts:
    #         print(x.name)
# ... Your code ...