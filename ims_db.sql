PGDMP     ;    3            
    {            ims01 %   12.15 (Ubuntu 12.15-0ubuntu0.20.04.1)    15.4 !    =           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            >           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            @           1262    140375    ims01    DATABASE     m   CREATE DATABASE ims01 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C.UTF-8';
    DROP DATABASE ims01;
                postgres    false            %          0    140407 
   auth_group 
   TABLE DATA                 public          admin    false    209   �       '          0    140417    auth_group_permissions 
   TABLE DATA                 public          admin    false    211   �       #          0    140399    auth_permission 
   TABLE DATA                 public          admin    false    207          )          0    140425 	   auth_user 
   TABLE DATA                 public          admin    false    213   r       +          0    140435    auth_user_groups 
   TABLE DATA                 public          admin    false    215          -          0    140443    auth_user_user_permissions 
   TABLE DATA                 public          admin    false    217          /          0    140503    django_admin_log 
   TABLE DATA                 public          admin    false    219   �       !          0    140389    django_content_type 
   TABLE DATA                 public          admin    false    205   �                 0    140378    django_migrations 
   TABLE DATA                 public          admin    false    203   �       :          0    140610    django_session 
   TABLE DATA                 public          admin    false    230   �!       1          0    140536    imsApp_category 
   TABLE DATA                 public          admin    false    221   8$       7          0    140573    imsApp_invoice 
   TABLE DATA                 public          admin    false    227   B%       9          0    140584    imsApp_invoice_item 
   TABLE DATA                 public          admin    false    229   C&       3          0    140547    imsApp_product 
   TABLE DATA                 public          admin    false    223   �&       5          0    140559    imsApp_stock 
   TABLE DATA                 public          admin    false    225   �(       Q           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          admin    false    208            R           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          admin    false    210            S           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);
          public          admin    false    206            T           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          admin    false    214            U           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);
          public          admin    false    212            V           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 20, true);
          public          admin    false    216            W           0    0    django_admin_log_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 2, true);
          public          admin    false    218            X           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);
          public          admin    false    204            Y           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);
          public          admin    false    202            Z           0    0    imsApp_category_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."imsApp_category_id_seq"', 2, true);
          public          admin    false    220            [           0    0    imsApp_invoice_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."imsApp_invoice_id_seq"', 3, true);
          public          admin    false    226            \           0    0    imsApp_invoice_item_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."imsApp_invoice_item_id_seq"', 4, true);
          public          admin    false    228            ]           0    0    imsApp_product_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."imsApp_product_id_seq"', 2, true);
          public          admin    false    222            ^           0    0    imsApp_stock_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."imsApp_stock_id_seq"', 7, true);
          public          admin    false    224            %   
   x���          '   
   x���          #   M  x���Mk�@E���K�D��EW%da()4i�B�G��i�����M��H�ޥ_D΁{�\���������7��.u���k���Z�}mu[Wk�W�V�i�nln?Z����Tz�ѝ�����gu����CѨ���Ŝ�{���Y���n��M��ϫ����/_��g��UؐB�/���3V!#��Z��	�G,~���8|J`G'K0S��-��3*����0s�] YΝZ��P��jr/K�ɔ?���9�b�S9G����Kz�u��?B��̙q)fz+Sfh
����G���Y����w�-%Mg�8d�<��(�_0��M�{^�_�_~��gvT�p����'���@��� � * 6�����p������ss�	��Gs/⇗T!�z�Bx@�Ћ�?(����3�PZ?��O���h�Iz��H�h�I�0�b�I���p��zk�7G>�w���F���������w=.�GO�y����y7u9��Mk;� �h�ExJj��ȀbGdb�E|�=�����Um�uTHdr�h��E�&�@��b'��lP&[��T�%�+�Z��M2      )   �  x�͐[O�0���+z�d{�0&b�e��4�頰X����z˶�zo�6o����q'�s7�dz�z��P�u5j�J��#Tʕ(Uʨ��L$|�.Y�l84��L1/��~YNy��U�8�$V�U�"Z�`!��E������at�Y�8�s��n�`�V{��-�����i�}*����ZD�p�2v�s>��}O���>��^2Cŝ�%���7�9��br��!� u-[��U��* ��To�s��_��S�5�9Z���?n���,��l�$0�ry�`��d`z!����d,���mM�a�K_��]�g�ź�w_f���n�,ҳ���~kv'�F9_~U�)�&�w�P��/�M�ʵn��>!;߭��س      +   
   x���          -   �   x��ӻ
�0��ݧȨ �c�N�b�ڮ���^�����}�~I��_U7�UU��T?^��:���it݀�w��:g�/�|{��;_~����f{(�K���$�ګ�_�QO9u�zƩ�sN=A���ӥ�#N=C]8���S/Pל�D�RZ5I���&qx�$���V V��
�Y�YC2+@kHhjIm�fV�y_�ys�      /   �   x�͏�n�0E���Q6�"�	Q���`��Ryl�L<�Ďb���^�J?����̝�)���
�����QU,OB׆�*�S�X�D��ܩ#0�V���c�����#��~�����v�w_�F�{/&�y}[ϗ0��aɔ�)#@�"%E��y>��쉐�`����4���PH�2,�r��|5���KP�'2�HF��4I�s�H��d�C7�𠰑��m���þU���l��C߅U�C      !   �   x���=k�0�ݿB�0�N��!��$Ф]�"	�Iw�#�_�d���m'�{^$]��o>��v��т�ӿ��+���ԧ� �I�[y4���K�����ŢmD-�_���P�¥^�W���~F�Lp#���n�!`&>����>������=��3_�s����|
��|/�D�d2r���̧�:��ǿ���P����~��?#(��m����qcHU�x�X�         �  x����N�0�=O���ȗĉ�+,�**��[�MLpǩ�Px����&U*��a`�8�Ϗ�����5����9��.W�O��V];�m��BWW�캫��Fm>l��.��7���>$�*9/m�U��k���p��B��k��k�������5ekDV9ei�? t~����B��ZJ�s��h$TF���C҉����a=�U8e�aHVȪ�E�)4*��� B��}�c#kQ>Y]��4��Ʊ�&�ym_�E�㴍�������P!���3�����7
#_D����O�
h[1�ѭm�Ã2R7KX|d|�J�Y�a30����A��h�ʎQ��}�tX���tEde�,<f��߃v��o��7��C_��&M�o��,]Io]�)�u¨���\_%�e�>:�'� �iNK�4�.gKmYn�F6����١[�ba����.,�.�L��ٗף������5.~L����l2�������7]��CW��{�S�nHe�^m�٢���k�8�|{ES�1����*bA���"�)B�Wj����&d����΅S_X�-͊r.�SI~�'�óWf�D(�0)���=eSK�S��f���Y���W�f\R$�7��M�U¾+�C���G��u���֢���0ֽ��5��)	�9结���_�?�=      :   �  x���˒�H��}=��)*�K���B� QA7��E.Y`"��]5��=�^�����cm<c�s��w9ʒ����2n�6�Ӿ/چ��s�n��������q�H�.�Z���Q���}{�`���꒸��=-�R�?����{}O��\���v�4*����*���y�Ț>Q���*]yz�]��3(��Nc�Q�V�d6`S�,���t�.����>�)��<���jt���ڕ���y�3�c�O烻і�:�1LиQπ�;�����j[m��L� �ϳ�pX�D���iŋ �ke���$�Vk\�a��h�y�:S��"dNPf�8��2�_ �~������T74i�q2��+o)�+�z�P��7�Qh�}�"�{K�e����ٙ.i{�q�b�$��U�-Q�
��ֆ�l�u��O�\�<����@�>�������*��� �z��򘴌�h4F��ÙzY�}�f�)��%[1�U�Z蠇�Y
Q�8Y�L����Y_�j�Fݲk��'��}�����J�|X���躱��~��g2�	�`	*�\��s�9��u��ĹZO�d��&4�o��|����B�.4#�_9e��G��U�`ш���5<>�@f�? 2� �?^^~ }7u�      1   �   x����j�@��>ŐK�q��]�)�P���j���Y��Ew}��Z(�Г�@��7�[�^�k.�������m�y� �f� ��gތ7�Z�+TU��ؼtAM�BYu��R�p�S��ݸ�;�V#�)iiP:���6)�ȅy����'������5/��E�+2�8X ��>�U��1�^Hh�WW��@q�CSp���Rfx�&}����N��M���{�?4���8-Ƙ�(��D��/D!��e��ނ�      7   �   x�ő�j�@��>Ő�	Uٙ5��9���PRh�^�]%,$��Zڷ�K���k;����1���{9B�?>C;�_�N��o��d�kt����"p]���v�6�w�Zw�ں�AU����z�jjC�Z����uw�%F#�Hl���@�1�%[O@�9�Y�R�=0��RRx`�	��3�[#���6�9���	���\$�g���������%ę?q��,!�(Ԭ��Y�"����s
��      9   �   x���v
Q���W((M��L�S��-v,(���+��LN��,I�UR��L�Q((
�(�&�d�T�(�Հ%�SJ�K�����l KS!��'�5XA�PG�,M�iZsy��r#��@k�,czZn��uӌ�����lj` ��4��� �S�'      3   �  x��RKn�0��D6rP� �OmweA��q����b"����d���E��I|�e����@��g��p�y�����Mf�[T�w��Leը,�Rq-���E���V�QE��pSW�FFBK0q��e��DK�<]j%��$�~�T��2�(�|��$�e�Њ�o��A9�<��T�y�3�U���k�uv'58J�ZC���=2�0���im��J�<kS;���Je���G���u������(�1�h8d�0�q�����̳�����j:ݷ��4�I�����Mo�ی��		��-�<ǛL`X����(���WGUo��Sg�ݧ�;���o9Jw?^P����) O�	<:�C��>!ﳠ�PvL��{4`�@���-V���z�	�� A:��ŉN�D�.h      5     x���;o�0�=��PM�{�҉�!RE�B�F4������o"�*��Ŗ�3|::�z�z�B��>���?�*�4_ǥ���W�5��O��n��Ġ=���۵uY��r�����몶l�ޖO��̐r�`��� Nb�� �r��4)��>pa�<p��q���ʁtås�$m���
D���� \���h�*�1��V�\���27�����g�݁�ܐ
l�0ʌ�S<��{
���e��Q��;�$�|�	����h<I~�ta     