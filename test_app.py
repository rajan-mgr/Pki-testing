import subprocess
def test_key_generation():

    result = subprocess.run(
    ["python", "app.py"],
    capture_output=True,
    text=True)
    
    output = result.stdout
    assert "Public Key:" in output
    assert "Private Key:" in output