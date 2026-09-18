from validators import validate_email, validate_age

def test_valid_email_accepted():
    assert validate_email("student@siam.ac.th") is True

def test_valid_email_with_subdomain():
    assert validate_email("user@mail.siam.ac.th") is True

def test_valid_age_accepted():
    assert validate_age(20) is True

def test_boundary_ages_accepted():
    assert validate_age(0) is True
    assert validate_age(150) is True


