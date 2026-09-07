import qrcode
choice = input("Want to generate QR code (y/n): ").lower().strip()
if choice == 'y':
	while(1):
		user_links = input("Enter all URL's separated by comma: ")
		links = [link.strip() for link in user_links.split(',')]
		for i, link in enumerate(links, start = 1):
			qr_name = input(f"Enter qr name for '{link}': ").strip()
			customizing = input("Want to edit colors (y/n): ").lower().strip()
			qr_code = qrcode.QRCode(version=1, box_size=10, border=4)
			qr_code.add_data(link)
			qr_code.make(fit=True)

			if customizing == "y":
				qr_color = input("Enter the color for your QR: ")
				qr_bg_color = input("Enter color for background of QR: ")
				img = qr_code.make_image(fill_color=qr_color, back_color=qr_bg_color)
			else:
				img = qr_code.make_image()

			img.save(qr_name)
		end = input("Want to continue generating (y/n): ")
		if end == 'n':
			break
		elif end == 'y':
			continue
		else:
			print("Invalid input!")
elif choice == 'n':
	print("Thank you!")



