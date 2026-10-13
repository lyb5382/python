inv = {"app": 15, "ban": 8, "org": 20, "mel": 3}
inv.update({"gra": 12})  # inv["gra"]=12
# inv['app']+=12
print("망고 재고:", inv.get("man", "재고 없음"))
# for i in inv:
#     print(f"과일: {i} | 재고: {inv[i]}")
for key, value in inv.items():
    print(f"과일: {key} | 재고: {value}개")