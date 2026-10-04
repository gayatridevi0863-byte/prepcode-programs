total_products = 157
box_capacity = 12

complete_boxes = total_products // box_capacity

remaining_products = total_products % box_capacity

print(f"Complete boxes filled: {complete_boxes}")
print(f"Products remaining: {remaining_products}")
