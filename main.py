from diaries.DiarySample import DiarySample
from diaries.OkuDiary import OkuDiary
from diaries.k23144 import k23144
from diaries.TakaiDiary import TakaiDiary
from diaries.RinoaDiary import RinoaDiary
from diaries.OhyamaDiary import OhyamaDiary
from diaries.MoriDiary import MoriDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    OkuDiary(),
    k23144(),
    TakaiDiary(),
    RinoaDiary(),
    OhyamaDiary(),
    MoriDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
# コミットのための追加