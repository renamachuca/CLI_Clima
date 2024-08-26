import subprocess

def test_weather_cli():
    result = subprocess.run(['python3', 'weather_cli.py', 'London,UK', '--format', 'text'], capture_output=True, text=True)
    assert "City:" in result.stdout
    assert "Temperature:" in result.stdout
    assert "Weather:" in result.stdout
