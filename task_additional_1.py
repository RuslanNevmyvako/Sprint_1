types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

tickets_by_type = {}

def deduplicate_issues(ticket_list, used_tickets):
    unique_tickets = []
    for ticket in ticket_list:
        if ticket not in used_tickets:
            unique_tickets.append(ticket)
            used_tickets.append(ticket)
    return unique_tickets

def tickets_type(types, tickets):
    used_tickets = []  # создаём список здесь
    for type_id, type_name in types.items():
        ticket_list = tickets.get(type_id, [])
        tickets_by_type[type_name] = deduplicate_issues(ticket_list, used_tickets)
    return tickets_by_type

tickets_type(types, tickets)
print(tickets_by_type)