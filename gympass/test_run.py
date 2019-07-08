from gympass.run import run


def test_flow():
    file = 'input.txt'
    results = run(file)
    expected_results = [
        '1 - 038 F.MASSA               4 laps - 00:04:11.578000',
        '2 - 002 K.RAIKKONEN           4 laps - 00:04:16.695000',
        '3 - 033 R.BARRICHELLO         4 laps - 00:04:17.161000',
        '4 - 023 M.WEBBER              4 laps - 00:04:20.550000',
        '5 - 015 F.ALONSO              4 laps - 00:05:01.316000',
        '6 - 011 S.VETTEL              2 laps - 00:05:34.235000'
    ]
    for item in results:
        assert str(item) in expected_results
