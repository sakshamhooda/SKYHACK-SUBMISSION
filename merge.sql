SELECT *
FROM inventory
LEFT OUTER JOIN pre_order ON 
    inventory.flight_number = pre_order.flight_number AND
    inventory.scheduled_departure_dtl = pre_order.scheduled_departure_dtl AND
    inventory.departure_station_code = pre_order.departure_station_code AND
    inventory.arrival_station_code = pre_order.arrival_station_code
LEFT OUTER JOIN satisfaction ON 
    inventory.flight_number = satisfaction.flight_number AND
    inventory.scheduled_departure_dtl = satisfaction.scheduled_departure_date AND
    inventory.departure_station_code = satisfaction.origin_station_code AND
    inventory.arrival_station_code = satisfaction.destination_station_code
LEFT OUTER JOIN comments ON 
    inventory.flight_number = comments.flight_number AND
    inventory.scheduled_departure_dtl = comments.scheduled_departure_date AND
    inventory.departure_station_code = comments.origin_station_code AND
    inventory.arrival_station_code = comments.destination_station_code;
