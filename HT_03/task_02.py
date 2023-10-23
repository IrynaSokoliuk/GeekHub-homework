'''
Write a script to remove an empty elements from a list.
Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
'''

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

filtered_list = [item for item in test_list if item]

print(f"New list: {filtered_list}")
