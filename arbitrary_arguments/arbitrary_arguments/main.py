def generate_report(*scores, **opset):
    label = opset.get('label', 'Report')
    avg = sum(scores)/len(scores)
    print(f'opset items = {opset.items()}')
    if 'passing_score' in opset.keys():
        status = 'Pass' if avg >= opset.get('passing_score',0) else 'Fail'
        return f'{label} | Average: {avg:.2f} | Status: {status}'

    return f'{label} | Average: {avg:.2f}'

# Testing the result
print(generate_report(80, 90, 70, label='Math', passing_score=75))
print(generate_report(50, 60, 40, passing_score=65))
print(generate_report(95, 88, 92, label='Science'))