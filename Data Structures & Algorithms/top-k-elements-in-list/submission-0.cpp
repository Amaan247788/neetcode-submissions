class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;

        for (int &num : nums) {
            freq[num]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minheap;

        for (auto& entry : freq) {
            minheap.push({entry.second, entry.first});
            if (minheap.size() > k) {
                minheap.pop();
            }
        }

        vector<int> ans;

        while (!minheap.empty()) {
            ans.push_back(minheap.top().second);
            minheap.pop();
        }

        return ans;

    }
};
