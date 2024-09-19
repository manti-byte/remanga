with open('like_posts.txt', 'w') as file:
    for i in range(676600, 676758):
        file.write(f'{i}\n')
    print('done')
