from bfv.batch_encoder import BatchEncoder
from bfv.bfv_decryptor import BFVDecryptor
from bfv.bfv_encryptor import BFVEncryptor
from bfv.bfv_evaluator import BFVEvaluator
from bfv.bfv_key_generator import BFVKeyGenerator
from bfv.bfv_parameters import BFVParameters

def main():

    degree = 4
    plain_modulus = 97
    ciph_modulus = 8000000000000
    params = BFVParameters(poly_degree=degree,
                           plain_modulus=plain_modulus,
                           ciph_modulus=ciph_modulus)
    key_generator = BFVKeyGenerator(params)
    public_key = key_generator.public_key
    secret_key = key_generator.secret_key
    relin_key = key_generator.relin_key
    encoder = BatchEncoder(params)
    encryptor = BFVEncryptor(params, public_key)
    decryptor = BFVDecryptor(params, secret_key)
    evaluator = BFVEvaluator(params)

    message1 = [10,18,0,7]
    message2 = [1, 5, 4,6]

    plain1 = encoder.encode(message1)
    plain2 = encoder.encode(message2)
    ciph1 = encryptor.encrypt(plain1)
    ciph2 = encryptor.encrypt(plain2)
    ciph_prod = evaluator.multiply(ciph1, ciph2, relin_key)
    ciph_sum = evaluator.add(ciph1,ciph2)
    decrypted_sum = decryptor.decrypt(ciph_sum)
    decrypted_prod = decryptor.decrypt(ciph_prod)
    decoded_prod = encoder.decode(decrypted_prod)
    decoded_sum = encoder.decode(decrypted_sum)
    
    print(decoded_prod)
    print(decoded_sum)

if __name__ == '__main__':
    main()
