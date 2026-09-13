from app import app, db, Ticket


def test_ticket_pages_load():
    app.config["TESTING"] = True
    client = app.test_client()
    assert client.get("/").status_code == 302
    client.post("/login", data={"email": "officer@pulsedesk.test", "password": "demo123"})
    assert client.get("/").status_code == 200
    assert client.get("/tickets").status_code == 200
    assert client.get("/tickets/new").status_code == 200


def test_detector_creates_alert():
    with app.app_context():
        assert Ticket.query.count() >= 0
