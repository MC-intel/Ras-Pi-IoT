#!/bin/bash
cd /home/pi/Desktop/GasExchange;  python3 -m http.server 8001 &
#!/bin/bash
rm data.json ; rm myresultsp.pickle