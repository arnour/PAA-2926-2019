from hamcrest import (
    assert_that,
    equal_to,
    close_to,
    empty
)
from paa191t1.pph import Pair
from paa191t1.tests import TestBase


class TestPPHBase(TestBase):

    def setUp(self):
        self.pph = lambda n, t: None

    def test_should_define_s(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8)
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.05))

        s = self.pph(n, Pair(4, 8))

        assert_that(
            s.values,
            equal_to([
                Pair(6, 6)
            ])
        )

        assert_that(s.r, close_to(0.71, delta=0.05))

    def test_should_define_s_empty(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(100, 10))

        assert_that(s.values, empty())
        assert_that(s.r, equal_to(10.0))

        n = [
            Pair(2, 15),
            Pair(3, 10),
            Pair(8, 19),
            Pair(3, 5),
            Pair(2, 9),
            Pair(6, 12)
        ]

        s = self.pph(n, Pair(6, 6))

        assert_that(s.values, empty())
        assert_that(s.r, equal_to(1.0))

    def test_should_add_all_n_in_s_and_n_is_sorted(self):
        n = [
            Pair(4, 3),
            Pair(7, 5),
            Pair(6, 4),
            Pair(8, 5),
            Pair(5, 3),
            Pair(9, 5)
        ]

        s = self.pph(n, Pair(1, 5))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(9, 5),
                Pair(5, 3),
                Pair(8, 5),
                Pair(6, 4),
                Pair(7, 5)
            ])
        )

        assert_that(s.r, close_to(1.33, delta=0.05))

        n = [Pair(i * i, i) for i in range(1, 150)]

        s = self.pph(n, Pair(15, 3))
        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(22201, 149),
                Pair(21904, 148)
            ])
        )

        assert_that(s.r, close_to(147.06, delta=0.01))

    def test_should_add_all_n_in_s_and_n_is_sorted_reversed(self):
        n = [
            Pair(9, 5),
            Pair(5, 3),
            Pair(8, 5),
            Pair(6, 4),
            Pair(7, 5),
            Pair(4, 3)
        ]

        s = self.pph(n, Pair(1, 5))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(9, 5),
                Pair(5, 3),
                Pair(8, 5),
                Pair(6, 4),
                Pair(7, 5)
            ])
        )

        assert_that(s.r, close_to(1.33, delta=0.05))

    def test_should_add_all_n_in_s_and_n_is_NOT_sorted(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(10, 100))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8),
                Pair(1, 3),
                Pair(5, 16)
            ])
        )

        assert_that(s.r, close_to(0.19, delta=0.05))

    def test_should_works_removing_all_elements_except_one(self):
        n = [
            Pair(5, 16),
            Pair(2, 5),
            Pair(1, 3),
            Pair(16, 16),
            Pair(3, 9),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(16, 16)
            ])
        )

        assert_that(s.r, close_to(0.54, delta=0.05))

    def test_should_works_removing_all_elements_except_one2(self):
        n = [
            Pair(5, 16),
            Pair(2, 5),
            Pair(1, 2),
            Pair(16, 16),
            Pair(3, 9),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(16, 16)
            ])
        )

        assert_that(s.r, close_to(0.54, delta=0.05))

    def test_should_works_with_poggi_trials(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8)
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.01))

    def test_should_works_with_huge_trials(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(772, 733),
            Pair(529, 986),
            Pair(282, 743),
            Pair(593, 636),
            Pair(652, 309),
            Pair(700, 549),
            Pair(493, 530),
            Pair(727, 357),
            Pair(640, 781),
            Pair(400, 223),
            Pair(87, 522),
            Pair(506, 996),
            Pair(604, 543),
            Pair(741, 203),
            Pair(223, 947),
            Pair(968, 821),
            Pair(977, 194),
            Pair(931, 855),
            Pair(221, 185),
            Pair(962, 178),
            Pair(472, 497),
            Pair(989, 963),
            Pair(283, 514),
            Pair(633, 74),
            Pair(441, 558),
            Pair(210, 990),
            Pair(515, 41),
            Pair(214, 708),
            Pair(110, 497),
            Pair(682, 337),
            Pair(860, 707),
            Pair(415, 809),
            Pair(524, 128),
            Pair(889, 774),
            Pair(11, 160),
            Pair(681, 136),
            Pair(713, 914),
            Pair(394, 649),
            Pair(862, 61),
            Pair(426, 225),
            Pair(435, 441),
            Pair(667, 816),
            Pair(941, 411),
            Pair(456, 724),
            Pair(326, 866),
            Pair(620, 56),
            Pair(722, 627),
            Pair(368, 416),
            Pair(597, 984),
            Pair(433, 19),
            Pair(507, 165),
            Pair(703, 363),
            Pair(863, 59),
            Pair(313, 974),
            Pair(695, 17),
            Pair(744, 742),
            Pair(278, 650),
            Pair(835, 657),
            Pair(522, 576),
            Pair(695, 500),
            Pair(682, 936),
            Pair(969, 595),
            Pair(552, 664),
            Pair(32, 533),
            Pair(702, 535),
            Pair(834, 790),
            Pair(868, 66),
            Pair(1000, 737),
            Pair(820, 221),
            Pair(118, 96),
            Pair(236, 215),
            Pair(109, 780),
            Pair(564, 812),
            Pair(43, 908),
            Pair(303, 873),
            Pair(721, 984),
            Pair(720, 108),
            Pair(112, 629),
            Pair(694, 332),
            Pair(209, 127),
            Pair(900, 223),
            Pair(932, 159),
            Pair(695, 257),
            Pair(41, 352),
            Pair(933, 148),
            Pair(848, 834),
            Pair(65, 494),
            Pair(231, 294),
            Pair(471, 642),
            Pair(600, 872),
            Pair(943, 952),
            Pair(369, 169),
            Pair(90, 907),
            Pair(621, 929),
            Pair(972, 649),
            Pair(591, 290),
            Pair(933, 813),
            Pair(195, 601),
            Pair(631, 405),
            Pair(553, 412),
            Pair(273, 187),
            Pair(559, 636),
            Pair(355, 528),
            Pair(165, 505),
            Pair(446, 660),
            Pair(711, 712),
            Pair(69, 494),
            Pair(475, 742),
            Pair(357, 754),
            Pair(611, 254),
            Pair(297, 944),
            Pair(327, 590),
            Pair(602, 265),
            Pair(451, 897),
            Pair(317, 237),
            Pair(832, 558),
            Pair(493, 770),
            Pair(195, 978),
            Pair(740, 2),
            Pair(893, 413),
            Pair(298, 141),
            Pair(927, 633),
            Pair(453, 139),
            Pair(310, 993),
            Pair(876, 222),
            Pair(318, 368),
            Pair(261, 760),
            Pair(192, 58),
            Pair(99, 16),
            Pair(793, 932),
            Pair(172, 968),
            Pair(759, 564),
            Pair(643, 305),
            Pair(623, 320),
            Pair(992, 997),
            Pair(224, 874),
            Pair(337, 103),
            Pair(388, 540),
            Pair(786, 113),
            Pair(607, 751),
            Pair(627, 521),
            Pair(46, 339),
            Pair(398, 121),
            Pair(237, 839),
            Pair(653, 947),
            Pair(983, 454),
            Pair(914, 124),
            Pair(911, 161),
            Pair(756, 669),
            Pair(105, 65),
            Pair(650, 496),
            Pair(182, 829),
            Pair(635, 253),
            Pair(248, 386),
            Pair(264, 507),
            Pair(219, 591),
            Pair(3, 529),
            Pair(228, 433),
            Pair(133, 456),
            Pair(888, 688),
            Pair(888, 346),
            Pair(985, 615),
            Pair(238, 258),
            Pair(23, 846),
            Pair(652, 145),
            Pair(264, 832),
            Pair(981, 621),
            Pair(246, 275),
            Pair(194, 450),
            Pair(231, 195),
            Pair(193, 238),
            Pair(473, 798),
            Pair(464, 412),
            Pair(732, 477),
            Pair(360, 679),
            Pair(690, 3),
            Pair(598, 933),
            Pair(277, 346),
            Pair(689, 100),
            Pair(663, 252),
            Pair(926, 244),
            Pair(919, 134),
            Pair(147, 975),
            Pair(936, 921),
            Pair(159, 591),
            Pair(104, 971),
            Pair(356, 935),
            Pair(734, 36),
            Pair(354, 333),
            Pair(9, 865),
            Pair(97, 924),
            Pair(922, 895),
            Pair(58, 608),
            Pair(524, 891),
            Pair(59, 240),
            Pair(552, 234),
            Pair(315, 499),
            Pair(100, 889),
            Pair(591, 28),
            Pair(695, 651),
            Pair(157, 887),
            Pair(376, 604),
            Pair(554, 545),
            Pair(929, 402),
            Pair(214, 590),
            Pair(889, 809),
            Pair(655, 381),
            Pair(333, 314),
            Pair(266, 10),
            Pair(885, 129),
            Pair(362, 9),
            Pair(647, 111),
            Pair(181, 951),
            Pair(938, 742),
            Pair(847, 420),
            Pair(508, 869),
            Pair(614, 849),
            Pair(19, 467),
            Pair(209, 354),
            Pair(874, 54),
            Pair(516, 467),
            Pair(531, 621),
            Pair(564, 970),
            Pair(743, 559),
            Pair(999, 118),
            Pair(944, 974),
            Pair(796, 703),
            Pair(864, 104),
            Pair(628, 12),
            Pair(903, 450),
            Pair(647, 853),
            Pair(690, 933),
            Pair(325, 947),
            Pair(948, 819),
            Pair(384, 871),
            Pair(842, 29),
            Pair(447, 879),
            Pair(214, 98),
            Pair(224, 146),
            Pair(250, 643),
            Pair(16, 392),
            Pair(677, 597),
            Pair(238, 184),
            Pair(729, 824),
            Pair(608, 402),
            Pair(102, 320),
            Pair(600, 726),
            Pair(332, 324),
            Pair(644, 136),
            Pair(20, 155),
            Pair(717, 212),
            Pair(240, 567),
            Pair(896, 314),
            Pair(987, 656),
            Pair(138, 183),
            Pair(361, 6),
            Pair(493, 115),
            Pair(903, 140),
            Pair(205, 242),
            Pair(847, 447),
            Pair(273, 225),
            Pair(522, 446),
            Pair(477, 195),
            Pair(183, 416),
            Pair(33, 653),
            Pair(779, 419),
            Pair(104, 692),
            Pair(758, 65),
            Pair(322, 734),
            Pair(276, 595),
            Pair(857, 10),
            Pair(459, 99),
            Pair(852, 643),
            Pair(406, 662),
            Pair(262, 988),
            Pair(613, 472),
            Pair(333, 789),
            Pair(90, 852),
            Pair(790, 264),
            Pair(566, 262),
            Pair(707, 675),
            Pair(912, 652),
            Pair(643, 329),
            Pair(49, 175),
            Pair(545, 479),
            Pair(449, 88),
            Pair(880, 205),
            Pair(934, 203),
            Pair(508, 413),
            Pair(781, 954),
            Pair(645, 738),
            Pair(247, 8),
            Pair(189, 567),
            Pair(200, 386),
            Pair(600, 107),
            Pair(306, 993),
            Pair(695, 762),
            Pair(194, 89),
            Pair(944, 405),
            Pair(798, 522),
            Pair(732, 432),
            Pair(919, 439),
            Pair(179, 472),
            Pair(276, 551),
            Pair(981, 408),
            Pair(449, 519),
            Pair(929, 703),
            Pair(592, 524),
            Pair(623, 634),
            Pair(671, 699),
            Pair(403, 626),
            Pair(428, 130),
            Pair(773, 137),
            Pair(233, 422),
            Pair(350, 533),
            Pair(459, 532),
            Pair(394, 867),
            Pair(238, 512),
            Pair(703, 366),
            Pair(925, 350),
            Pair(768, 11),
            Pair(595, 926),
            Pair(756, 612),
            Pair(413, 795),
            Pair(300, 272),
            Pair(54, 607),
            Pair(243, 622),
            Pair(128, 551),
            Pair(485, 42),
            Pair(459, 73),
            Pair(937, 119),
            Pair(831, 444),
            Pair(981, 790),
            Pair(820, 88),
            Pair(331, 971),
            Pair(551, 784),
            Pair(915, 99),
            Pair(232, 537),
            Pair(971, 926),
            Pair(472, 850),
            Pair(136, 695),
            Pair(178, 916),
            Pair(665, 367),
            Pair(402, 155),
            Pair(28, 974),
            Pair(632, 667),
            Pair(490, 161),
            Pair(539, 930),
            Pair(76, 477),
            Pair(254, 163),
            Pair(627, 26),
            Pair(2, 24),
            Pair(294, 967),
            Pair(663, 256),
            Pair(56, 316),
            Pair(951, 133),
            Pair(239, 284),
            Pair(237, 69),
            Pair(72, 918),
            Pair(218, 317),
            Pair(847, 506),
            Pair(88, 518),
            Pair(165, 678),
            Pair(652, 838),
            Pair(521, 435),
            Pair(227, 615),
            Pair(812, 51),
            Pair(286, 809),
            Pair(137, 392),
            Pair(754, 855),
            Pair(7, 262),
            Pair(978, 379),
            Pair(163, 573),
            Pair(197, 606),
            Pair(76, 329),
            Pair(470, 618),
            Pair(966, 263),
            Pair(708, 352),
            Pair(230, 182),
            Pair(31, 632),
            Pair(219, 92),
            Pair(129, 29),
            Pair(856, 247),
            Pair(282, 865),
            Pair(660, 127),
            Pair(320, 858),
            Pair(531, 195),
            Pair(295, 918),
            Pair(291, 537),
            Pair(7, 551),
            Pair(391, 273),
            Pair(969, 543),
            Pair(496, 850),
            Pair(240, 641),
            Pair(997, 77),
            Pair(509, 741),
            Pair(524, 841),
            Pair(843, 799),
            Pair(143, 454),
            Pair(59, 190),
            Pair(717, 693),
            Pair(738, 464),
            Pair(389, 520),
            Pair(298, 870),
            Pair(800, 798),
            Pair(646, 264),
            Pair(955, 364),
            Pair(683, 577),
            Pair(233, 581),
            Pair(187, 228),
            Pair(4, 794),
            Pair(545, 371),
            Pair(298, 785),
            Pair(205, 19),
            Pair(251, 885),
            Pair(781, 526),
            Pair(172, 727),
            Pair(423, 61),
            Pair(641, 754),
            Pair(254, 81),
            Pair(581, 355),
            Pair(909, 615),
            Pair(766, 710),
            Pair(761, 5),
            Pair(174, 451),
            Pair(778, 580),
            Pair(423, 51),
            Pair(865, 912),
            Pair(337, 158),
            Pair(985, 468),
            Pair(700, 461),
            Pair(955, 749),
            Pair(774, 587),
            Pair(637, 770),
            Pair(677, 275),
            Pair(49, 207),
            Pair(128, 504),
            Pair(950, 282),
            Pair(404, 824),
            Pair(625, 870),
            Pair(839, 688),
            Pair(556, 156),
            Pair(760, 861),
            Pair(898, 428),
            Pair(335, 996),
            Pair(589, 472),
            Pair(820, 955),
            Pair(927, 957),
            Pair(842, 985),
            Pair(423, 722),
            Pair(867, 778),
            Pair(559, 304),
            Pair(676, 661),
            Pair(101, 142),
            Pair(722, 633),
            Pair(936, 78),
            Pair(795, 593),
            Pair(179, 829),
            Pair(116, 503),
            Pair(731, 929),
            Pair(366, 881),
            Pair(956, 810),
            Pair(1000, 93),
            Pair(744, 329),
            Pair(695, 758),
            Pair(213, 619),
            Pair(465, 491),
            Pair(101, 862),
            Pair(475, 636),
            Pair(880, 116),
            Pair(703, 269),
            Pair(769, 650),
            Pair(990, 152),
            Pair(68, 370),
            Pair(107, 423),
            Pair(835, 348),
            Pair(177, 486),
            Pair(481, 957),
            Pair(410, 822),
            Pair(382, 928),
            Pair(531, 731),
            Pair(846, 180),
            Pair(115, 707),
            Pair(542, 967),
            Pair(616, 355),
            Pair(502, 914),
            Pair(422, 260),
            Pair(433, 341),
            Pair(768, 908),
            Pair(980, 972),
            Pair(407, 462),
            Pair(538, 945),
            Pair(254, 302),
            Pair(194, 998),
            Pair(113, 165),
            Pair(758, 516),
            Pair(229, 376),
            Pair(946, 167),
            Pair(77, 913),
            Pair(861, 17),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(740, 2),
                Pair(690, 3),
                Pair(761, 5),
                Pair(857, 10)
            ])
        )

        assert_that(s.r, close_to(82.43, delta=0.01))
