class People(list):
    def print_stats(self, rounding=0, full=False):
        sorted_people = sorted(self, key=lambda p: p.cash, reverse=True)
        top_10_alices = sum(1 for p in sorted_people[:10] if p.name == "Alice") / 10 * 100
        top_100_alices = sum(1 for p in sorted_people[:100] if p.name == "Alice") / 100 * 100
        decile_count = len(sorted_people) // 10
        top_decile_alices = sum(1 for p in sorted_people[:decile_count] if p.name == "Alice") / decile_count * 100
        surviving_alices = [p.cash for p in sorted_people if p.name == "Alice" and p.cash > 0]
        surviving_bobs = [p.cash for p in sorted_people if p.name == "Bob" and p.cash > 0]

        print(f"% Alices in top 10: {round(top_10_alices, rounding)}%")
        print(f"% Alices in top 100: {round(top_100_alices, rounding)}%")
        print(f"% Alices in top decile: {round(top_decile_alices, rounding)}%")
        if surviving_alices:
            print(f"Surviving Alices' avg: {round(sum(surviving_alices) / len(surviving_alices), rounding)}")
        if surviving_bobs:
            print(f"Surviving Bobs' avg: {round(sum(surviving_bobs) / len(surviving_bobs), rounding)}")
        print(f"Alices' avg: {round(sum(p.cash for p in sorted_people if p.name == 'Alice') / len([p for p in sorted_people if p.name == 'Alice']), rounding)}")
        print(f"Bobs' avg: {round(sum(p.cash for p in sorted_people if p.name == 'Bob') / len([p for p in sorted_people if p.name == 'Bob']), rounding)}")
