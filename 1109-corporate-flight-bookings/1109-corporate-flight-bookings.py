class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats_reserved = [0] * (n+2)
        for first, last, seat in bookings:
            seats_reserved[first] += seat
            seats_reserved[last + 1] -= seat
        
        for i in range(1, n+1):
            seats_reserved[i] += seats_reserved[i-1]
        
        return seats_reserved[1: n+1]