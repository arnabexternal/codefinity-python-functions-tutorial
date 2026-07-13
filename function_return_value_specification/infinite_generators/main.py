def id_generator():

    count = 1

    while count:

        yield f'ID_{str(count)}'

        count += 1

id_gen = id_generator()

# Testing the result
for identity in range(5):
    unique_id = next(id_gen)
    print(unique_id)