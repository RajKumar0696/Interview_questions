student = [{'id': 1, 'success': True, 'name': 'Larry'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(i["id"] for i in student))
print(sum(i['success'] for i in student))


sum_of_id = 0
sum_of_success = 0
for items in student:
    for key in items:
        if key == "id":
            sum_of_id += items[key]
        elif key == "success":
            sum_of_success += items[key]
print(sum_of_id)
print(sum_of_success)
