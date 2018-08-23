def show_item(final_list):
    result = []
    if final_list:
        for sublist in final_list:
            result.append(f"Manufacture is: {sublist['manufacturer']},"
                          f" Model is :{sublist['model']}: {sublist['model_number']}, GPU mGh: {sublist['gpu_mgh']}, GPU memory/MB: {sublist['gpu_memory_mb']},"
                          f" Price: {sublist['price']} \n ")
    else:
        print('________________________________')
        result.append('We did not find suitable graphics cards!')
    return result
