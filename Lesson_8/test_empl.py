from empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Denis"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Denis"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Denis1234", "K")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Denis1234"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "K"


def test_get_employee_by_id():
    name = "Denis"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Denis123", "Kl")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Denis123"
    assert get_info["lastName"] == "Kl"


def test_change_employee_info():
    name = "Denis123"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Denis123", "Klyavin")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Klyavin", "test2@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test2@mail.ru"
    assert update["isActive"] == True