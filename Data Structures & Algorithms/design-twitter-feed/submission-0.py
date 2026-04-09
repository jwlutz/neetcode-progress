import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.following[userId].copy()
        followees.add(userId)

        heap = []
        for f in followees:
            if self.tweets[f]:
                index = len(self.tweets[f]) - 1
                time, tweetId = self.tweets[f][index]
                heap.append((-time, tweetId, f, index))
        heapq.heapify(heap)

        result = []
        while heap and len(result) < 10:
            neg_time, tweetId, f, index = heapq.heappop(heap)
            result.append(tweetId)

            if index > 0:
                next_time, next_tweetId = self.tweets[f][index - 1]
                heapq.heappush(heap, (-next_time, next_tweetId, f, index - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
