###########################################################
#String of the school dung trong truy cap he thong  khi port 
string_post = "66540EEE-61D6-48E2-B9B6-61BA0228B0FD" #****
#String unitCode dinh danh ten truong, doanh nghiep
string_unitCode = "titkul"
#UUID of the device 
uuid_device = "2db5af4f-ed76-390e-9b71-e5704b0fd1a8"                                            #****
#API get on the school system to create data 5 json
url_hanet = "https://api-hr.systemkul.com/v1/NhanVien/Kiosk"                       #****
#API get the getway informations to create data 3 json
ulr_getway = 'https://gateway-staging.systemkul.com/api/Gateway/GetListPeopleByUnit'         #****
#API upload data to  server when having temperature
url_upload_data = "https://api-hr.systemkul.com/api/Attendances/AttendanceByDevice"     #****
#CSVtamthoi trong  upload    
tamthoi_csv = "data/recognization.csv"
#CSVhistory trong upload.
history_csv = "data/hisory_bakup.csv"
#Json data3 when create
json_data3 = 'data/data3.json'
#Json data5 when create
json_data5 = 'data/data5.json'
###########################################################
#Time shutdowns
timeshutshown = "23:10"

#-----------------------SIGNALR----------------------------
url_signalR = "https://gateway-staging.systemkul.com/signalR"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjJkYjVhZjRmLWVkNzYtMzkwZS05YjcxLWU1NzA0YjBmZDFhOCIsIklkIjoiMmRiNWFmNGYtZWQ3Ni0zOTBlLTliNzEtZTU3MDRiMGZkMWE4IiwiZXhwIjoxNjQzMjU3MjE3LCJpc3MiOiJodHRwczovL3RpdGt1bC52biIsImF1ZCI6Imh0dHBzOi8vdGl0a3VsLnZuIn0.7JRdUIiKOUyYGe3KGevm5si6ZQP-I0ChK8w5O6dkjlo"

# https://api-vietthang.systemkul.com/api/Attendances/AttendanceByDevice

# https://api-vietthang.systemkul.com/v1/NhanVien/Kiosk