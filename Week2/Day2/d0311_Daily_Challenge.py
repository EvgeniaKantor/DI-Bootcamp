class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize)

    def paginate(self):
        paginated_items = []
        for i in range(0, len(self.items), self.pageSize):
            paginated_items.append(self.items[i:i + self.pageSize])
        return paginated_items

    def getVisibleItems(self):
        choose_page = int(input('Enter the number of the page: '))
        paginated_items = self.paginate()
        if 1 <= choose_page <= len(paginated_items):
            return paginated_items[choose_page - 1]
        else:
            print("This page number is out of range.")
            return []

    def prevPage(self, current_page):
        prev_page = current_page - 1
        if prev_page >= 1:
            return prev_page
        else:
            print("This page number is out of range.")
            return current_page

    def nextPage(self, current_page):
        next_page = current_page + 1
        if next_page <= len(self.paginate()):
            return next_page
        else:
            print("This page number is out of range.")
            return current_page

    def lastPage(self):
        paginated_items = self.paginate()
        if paginated_items:
            return paginated_items[-1]
        else:
            print("No items to paginate.")
            return []

    def firstPage(self):
        paginated_items = self.paginate()
        if paginated_items:
            return paginated_items[0]
        else:
            print("No items to paginate.")
            return []


# Example usage:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
