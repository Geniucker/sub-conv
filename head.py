head = """mixed-port: 7890
allow-lan: true
mode: Rule
log-level: info
external-controller: :9090
"""
pp = """proxy-providers:
  subscription:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  hk:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '๐ญ๐ฐ'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  sg:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '๐ธ๐ฌ'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  jp:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '๐ฏ๐ต'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
"""
pg = """proxy-groups:
  - name: ๐ ่็น้ๆฉ
    type: select
    proxies:
      - โป๏ธ ่ชๅจ้ๆฉ
      - ๐ฏ ๆ้่ฝฌ็งป
      - ๐ฎ ่ด่ฝฝๅ่กก
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐ ๆๅจๅๆข
    type: select
    use:
      - subscription
  - name: โป๏ธ ่ชๅจ้ๆฉ
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: ๐ฏ ๆ้่ฝฌ็งป
    type: fallback
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: ๐ฎ ่ด่ฝฝๅ่กก
    type: load-balance
    strategy: consistent-hashing
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: ๐ฒ ็ตๆฅๆถๆฏ
    type: select
    proxies:
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐น ๆฒน็ฎก่ง้ข
    type: select
    proxies:
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐ฅ ๅฅ้ฃ่ง้ข
    type: select
    proxies:
      - ๐ฅ ๅฅ้ฃ่็น
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐บ ๅทดๅๅง็น
    type: select
    proxies:
      - ๐ ่็น้ๆฉ
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐บ ๅๅฉๅๅฉ
    type: select
    proxies:
      - ๐ฏ ๅจ็็ด่ฟ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
  - name: ๐ ๅฝๅคๅชไฝ
    type: select
    proxies:
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
      - DIRECT
  - name: ๐ ๅฝๅๅชไฝ
    type: select
    proxies:
      - DIRECT
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: ๐ข ่ฐทๆญFCM
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: โ๏ธ ๅพฎ่ฝฏไบ็
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: โ๏ธ ๅพฎ่ฝฏๆๅก
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: ๐ ่นๆๆๅก
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: ๐ฎ ๆธธๆๅนณๅฐ
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: ๐ถ ็ฝๆ้ณไน
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
  - name: ๐ฏ ๅจ็็ด่ฟ
    type: select
    proxies:
      - DIRECT
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
  - name: ๐ ๅนฟๅๆฆๆช
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: ๐ ๅบ็จๅๅ
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: ๐ ๆผ็ฝไน้ฑผ
    type: select
    proxies:
      - ๐ ่็น้ๆฉ
      - โป๏ธ ่ชๅจ้ๆฉ
      - DIRECT
      - ๐ญ๐ฐ ้ฆๆธฏ่็น
      - ๐ธ๐ฌ ็ฎๅ่็น
      - ๐ฏ๐ต ๆฅๆฌ่็น
      - ๐บ๐ธ ็พๅฝ่็น
      - ๐ ๆๅจๅๆข
  - name: ๐ญ๐ฐ ้ฆๆธฏ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - hk
  - name: ๐ฏ๐ต ๆฅๆฌ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - jp
  - name: ๐บ๐ธ ็พๅฝ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - DIRECT
  - name: ๐จ๐ณ ๅฐๆนพ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - DIRECT
  - name: ๐ธ๐ฌ ็ฎๅ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - sg
  - name: ๐ฐ๐ท ้ฉๅฝ่็น
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - DIRECT
  - name: ๐ฅ ๅฅ้ฃ่็น
    type: select
    proxies:
      - DIRECT
"""
