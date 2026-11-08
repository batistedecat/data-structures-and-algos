# De code van je collega. Ze is correct, maar te traag op grote feeds.
# Herschrijf ze zodat ze hetzelfde doet en wel schaalt.

def merge_feeds(feed_a, feed_b):
    i = 0
    j = 0
    res = []
    while i != len(feed_a) and j != len(feed_b):
        if feed_a[i][0] == feed_b[j][0]:
            res.append([feed_a[i][0] , min(feed_a[i][1] , feed_b[j][1])])
            i += 1
            j += 1
        elif feed_a[i][0] < feed_b[j][0]:
            res.append([feed_a[i][0] , feed_a[i][1]])
            i += 1
        else:
            res.append([feed_b[j][0], feed_b[j][1]])
            j += 1
    res.extend(feed_a[i:])
    res.extend(feed_b[j:])
    return res

def moving_average(feed, window):
    if window <= 0 or window > len(feed):
        return []
    res = []
    prefix = [feed[0][1]]
    for i in range(1,len(feed)):
        prefix.append(feed[i][1] + prefix[-1])

    j = window - 1
    i = 0
    while j < len(feed):
        wsum = prefix[j] - prefix[i] + feed[i][1]
        wmean = round(float(wsum / float(window)), 2)
        res.append(wmean)
        i +=1
        j +=1
    return res

def largest_gap(feed):
    prefix = [feed[0][1]]
    for i in range(1, len(feed)):
        diff = feed[i][1] - feed[i-1][1]


def traagste_stap():
    # Geef hier de letter terug van de belangrijkste oorzaak, zie de opgave.
    return '?'


if __name__ == "__main__":
    print(merge_feeds([["2026-01-03", 5], ["2026-01-05", 8]],
                      [["2026-01-04", 6], ["2026-01-05", 7]]))
    # [['2026-01-03', 5], ['2026-01-04', 6], ['2026-01-05', 7]]

    print(merge_feeds([], [["2026-01-04", 6]]))
    # [['2026-01-04', 6]]

    print(merge_feeds([["2026-01-04", 6]], []))
    # [['2026-01-04', 6]]

    print(merge_feeds([], []))
    # []

    print(merge_feeds([["2026-01-05", 8]], [["2026-01-05", 7]]))
    # [['2026-01-05', 7]]

    print(merge_feeds([["2026-01-05", 3]], [["2026-01-05", 7]]))
    # [['2026-01-05', 3]]

    print(moving_average([['2026-01-02', 9.8], ['2026-01-05', 10.0], ['2026-01-09', 10.2], ['2026-01-15', 11.2], ['2026-01-20', 11.0]],3))

