.section .data
msg_menu:
	.asciz "\nSelecciona una opcion: \n1.Saludar\n2.Salir\n\n"
msg_opcion1:
	.asciz "\nHola Arqui1"
msg_opcion2:
	.asciz "\nSaliendo Arqui1"
buffer:
	.skip 1
	
.section .text
_start:
	mov x0, 1			// Establecer Salida
	ldr x1, =msg_menu	// Cargar el Mensaje Menu
	mov x2, 44
	mov x8, 64
	svc 0
	
	//Leer entrada de datos
	mov x0,0
	ldr x1, =buffer
	mov x2, 1
	mov x8, 63
	svc 0
	
	// Verificar la opcion seleccionada
	ldrb w3, [x1]
	cmp w3, '1'
	beq opcion1
	cmp w3, '2'
	beq opcion2
	
	b _start

opcion1:
	mov x0, 1
	ldr x1, =msg_opcion1
	mov x2, 12
	mov x8, 64
	svc 0
	b _start

opcion2:
	mov x0, 0
	ldr x1, =msg_opcion2
	mov x2, 16
	mov x8, 64
	svc 0
	
	mov x0, 0
	mov x8, 93
	svc 0
	