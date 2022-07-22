):
        random_rows.append(get_parent_row())
    random_rows.append("child")
    for i in range(options.NUM_ROWS_CHILD - inherited_rows):
        random_rows.append(random_row())
    writer.writerows(random_rows)