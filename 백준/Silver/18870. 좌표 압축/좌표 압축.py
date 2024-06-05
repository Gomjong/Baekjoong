def compress_coordinates(n, coordinates):
    # 중복 제거 후 정렬된 리스트 생성
    sorted_coords = sorted(set(coordinates))
    
    # 좌표 압축을 위한 사전 생성
    coord_dict = {coord: i for i, coord in enumerate(sorted_coords)}
    
    # 원래 좌표를 압축된 값으로 변환
    compressed = [coord_dict[coord] for coord in coordinates]
    
    return compressed

# 입력
n = int(input().strip())
coordinates = list(map(int, input().strip().split()))

# 좌표 압축
result = compress_coordinates(n, coordinates)

# 결과 출력
print(' '.join(map(str, result)))