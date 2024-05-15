from flask import Flask, request

app = Flask(__name__)

videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

def merge_sort(data):
    if len(data) > 1:   
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        l = r = m = 0
        while l < len(left) and r < len(right):
            if left[l]['title'] < right[r]['title']:
                data[m] = left[l]
                l += 1
            else:
                data[m] = right[r]
                r += 1
            m += 1
        while l < len(left):
            data[m] = left[l]
            l += 1
            m += 1
        while r < len(right):
            data[m] = right[r]
            r += 1
            m += 1
    return data

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['title'] == target: return data[mid]
        elif data[mid]['title'] < target: low = mid + 1
        else: high = mid - 1
    return None

@app.route('/')
def index(): return 'Hello World'

@app.route('/videos')
def search_videos():
    sorted_videos = merge_sort(videos)
    search = request.args.get('search', None)
    video = binary_search(sorted_videos, search)
    if not video: return ({'error': f'Video title {search} not found'}), 404
    return video 

@app.route('/sorted-vidoes')
def sorted_videos():
  sorted_videos = merge_sort(videos) 
  return [vid for vid in sorted_videos]

if __name__ == '__main__': app.run(debug=True)