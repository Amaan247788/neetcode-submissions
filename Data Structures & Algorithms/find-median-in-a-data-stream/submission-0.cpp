class MedianFinder {
private:
vector<int> nums;
public:
    MedianFinder() {
        nums.clear();
    }
    
    void addNum(int num) {
        nums.push_back(num);
    }
    
    double findMedian() {
        if (nums.size() == 1) return nums[0];
        sort(nums.begin(), nums.end());
        if ((nums.size() % 2) == 0) {
            int firstNum = nums[nums.size()/2];
            int secondNum = nums[(nums.size()/2) - 1];
            double median = firstNum + secondNum;
            median /= 2;
            return median;
        }
        return nums[nums.size()/2];
    }
};
