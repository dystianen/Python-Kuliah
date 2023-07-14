class simulation:
  courses = {
      'Pemrograman': {
          'ilmu_alam': 0,
          'ilmu_sosial': 0,
          'pemrograman': 1,
          'teknologi': 1,
          'praktis': 1,
          'teoritis': 0,
          'minat_khusus': 0
      },
      'Sains Lingkungan': {
          'ilmu_alam': 1,
          'ilmu_sosial': 0,
          'pemrograman': 0,
          'teknologi': 0,
          'praktis': 1,
          'teoritis': 1,
          'minat_khusus': 0
      },
      'Seni Rupa': {
          'ilmu_alam': 0,
          'ilmu_sosial': 1,
          'pemrograman': 0,
          'teknologi': 0,
          'praktis': 1,
          'teoritis': 1,
          'minat_khusus': 1
      }
  }

  print("Selamat datang di simulasi penentuan mata kuliah yang paling disukai!")
  print("Silakan jawab pertanyaan berikut untuk mendapatkan rekomendasi mata kuliah:")
  print()

  ilmu_alam = int(input("Apakah Anda lebih suka mata kuliah yang berfokus pada ilmu alam? (0: Tidak, 1: Ya): "))
  ilmu_sosial = int(input("Apakah Anda lebih suka mata kuliah yang berfokus pada ilmu sosial? (0: Tidak, 1: Ya): "))
  pemrograman = int(input("Apakah Anda tertarik pada mata kuliah yang melibatkan pemrograman? (0: Tidak, 1: Ya): "))
  teknologi = int(input("Apakah Anda tertarik pada mata kuliah yang melibatkan teknologi? (0: Tidak, 1: Ya): "))
  praktis = int(input("Apakah Anda lebih suka mata kuliah yang praktis? (0: Tidak, 1: Ya): "))
  teoritis = int(input("Apakah Anda lebih suka mata kuliah yang teoritis? (0: Tidak, 1: Ya): "))
  minat_khusus = int(input("Apakah Anda memiliki minat khusus dalam bidang tertentu? (0: Tidak, 1: Ya): "))

  scores = {}
  for course, attributes in courses.items():
      score = 0
      if attributes['ilmu_alam'] == ilmu_alam:
          score += 1
      if attributes['ilmu_sosial'] == ilmu_sosial:
          score += 1
      if attributes['pemrograman'] == pemrograman:
          score += 1
      if attributes['teknologi'] == teknologi:
          score += 1
      if attributes['praktis'] == praktis:
          score += 1
      if attributes['teoritis'] == teoritis:
          score += 1
      if attributes['minat_khusus'] == minat_khusus:
          score += 1
      scores[course] = score

  sorted_courses = sorted(scores, key=scores.get, reverse=True)

  print("\nBerikut rekomendasi mata kuliah berdasarkan preferensi Anda:")
  for course in sorted_courses:
      print(f"- {course}")