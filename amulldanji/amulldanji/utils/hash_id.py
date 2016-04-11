from hashids import Hashids


def get_encoded_hash_id(instance):
    hashids_salt = Hashids(
        salt=instance._meta.model_name,
        min_length=4,
    )
    hash_id = hashids_salt.encode(instance.id)

    return hash_id
