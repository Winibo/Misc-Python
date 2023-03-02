articles, rating = [int(x)for x in input().split(" ")]
citations = articles*rating
answer = citations-(articles-1)
print(answer)
