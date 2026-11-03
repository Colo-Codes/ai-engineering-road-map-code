codes = {200, 404}
codes.add(500)
print(codes)
codes.add(200)
print(codes, len(codes))

# .discard() removes a member, and does nothing for a missing value
codes.discard(404)
print(codes)
codes.discard(301)
print(codes)

# .remove() removes a member, and stops the script for a missing value
codes.remove(500)
print(codes)
# codes.remove(301)
codes.discard(301)
print(codes)
