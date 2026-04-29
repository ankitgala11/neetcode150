class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(list)
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.timer))
        self.timer += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        temp.extend(self.posts[userId])
        # print(self.follows, userId)
        for followerId in self.follows[userId]:
            temp.extend(self.posts[followerId])
        temp.sort(key = lambda x : -x[1])
        ans = []
        cnt = 0
        for i, x in temp:
            if cnt>=10:break
            ans.append(i)
            cnt += 1

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.follows[followerId]:return
        self.follows[followerId].append(followeeId)
        # print("here:", self.follows)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.follows[followerId]:return
        self.follows[followerId].remove(followeeId)

        
