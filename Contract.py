import hmac
import hashlib
import random
import time

class CONTRACT:
    def __init__(self, c_id, amt, i_id, u_id):
        self.contract_id = c_id
        self.amount = amt
        self.issuer_id = i_id
        self.user_id = u_id

        self.private_key = self.make_key(self.contract_id,self.amount,self.issuer_id,self.user_id)  #c_id + str(amt) + i_id + u_id
        self.challenge = None
        self.hmac = None
        self.random_bit = None

        
    # def make_key(self, c_id, amt, i_id, u_id):
    #     return c_id + str(amt) + i_id + u_id

    def make_key(self, c_id, amt, i_id, u_id):
        dt = c_id + str(amt) + i_id + u_id
        key = self.doSomeHash(dt)
        return key

    def generate_challenge(self):
        self.challenge = ''.join([chr(random.randint(0, 255)) for _ in range(16)])

    def set_rand_bit(self, bit):
        self.random_bit = bit

    def create_hmac(self):
        combined_data = self.challenge + str(self.random_bit)
        hmac_result = hmac.new(self.private_key.encode(), combined_data.encode(), hashlib.sha256).hexdigest()
        self.hmac = hmac_result

    def doSomeHash(self,data):
        hash1 = hashlib.sha256(data.encode()).hexdigest()
        hash2 = hashlib.sha256("For_Key_Maker".encode()).hexdigest()
        combined = str(int(hash1, 16) ^ int(hash2, 16))
        return combined