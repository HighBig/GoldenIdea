from django.core.management.base import BaseCommand
from accounts.models import Department, User


def create_user(username, name, department_id):
    department = Department.objects.get(id=department_id)
    user = User()
    user.username = username
    user.name = name
    user.department = department
    user.set_password('')
    user.save()


class Command(BaseCommand):
    help = 'Create user'

    users = [
        # 管理层
        {
            'department_id': 1,
            'username': 'shajiliang',
            'name': '沙纪良',
        },
        {
            'department_id': 1,
            'username': 'guguoyin',
            'name': '顾国银',
        },
        {
            'department_id': 1,
            'username': 'jinxing',
            'name': '金星',
        },
        {
            'department_id': 1,
            'username': 'yuanhui',
            'name': '袁晖',
        },

        # 综合管理部
        {
            'department_id': 2,
            'username': 'hanweiguo',
            'name': '韩维国',
        },
        {
            'department_id': 2,
            'username': 'zhanglin',
            'name': '章琳',
        },
        {
            'department_id': 2,
            'username': 'caoweining',
            'name': '曹伟宁',
        },
        {
            'department_id': 2,
            'username': 'shixiaoping',
            'name': '史小平',
        },
        {
            'department_id': 2,
            'username': 'tubin',
            'name': '涂斌',
        },
        {
            'department_id': 2,
            'username': 'wangxueqin',
            'name': '王雪琴',
        },
        {
            'department_id': 2,
            'username': 'zhoumiaoqiong',
            'name': '周苗琼',
        },

        # 开发建设事业部
        {
            'department_id': 3,
            'username': 'zhufucun',
            'name': '朱福存',
        },
        {
            'department_id': 3,
            'username': 'wangxudong',
            'name': '王旭东',
        },
        {
            'department_id': 3,
            'username': 'caiyunjie',
            'name': '蔡云杰',
        },
        {
            'department_id': 3,
            'username': 'chenxunliang',
            'name': '陈训良',
        },
        {
            'department_id': 3,
            'username': 'jinhao',
            'name': '金昊',
        },
        {
            'department_id': 3,
            'username': 'luoshuai',
            'name': '罗帅',
        },
        {
            'department_id': 3,
            'username': 'wanghaoran',
            'name': '汪皓然',
        },
        {
            'department_id': 3,
            'username': 'wangjie',
            'name': '王捷',
        },
        {
            'department_id': 3,
            'username': 'wugang',
            'name': '邬刚',
        },
        {
            'department_id': 3,
            'username': 'yinxiaocun',
            'name': '尹小存',
        },
        {
            'department_id': 3,
            'username': 'zhangjiangang',
            'name': '张键钢',
        },
    
        # 售电服务事业部
        {
            'department_id': 4,
            'username': 'chenminfeng',
            'name': '陈敏峰',
        },
        {
            'department_id': 4,
            'username': 'fengjiemin',
            'name': '冯洁民',
        },
        {
            'department_id': 4,
            'username': 'xuxiao',
            'name': '徐晓',
        },
        {
            'department_id': 4,
            'username': 'caijie',
            'name': '蔡洁',
        },
        {
            'department_id': 4,
            'username': 'chenge',
            'name': '陈鸽',
        },
        {
            'department_id': 4,
            'username': 'chenyongyong',
            'name': '陈永勇',
        },
        {
            'department_id': 4,
            'username': 'dingdongbo',
            'name': '丁东波',
        },
        {
            'department_id': 4,
            'username': 'dongliujie',
            'name': '董柳杰',
        },
        {
            'department_id': 4,
            'username': 'fanxiaobin',
            'name': '范晓斌',
        },
        {
            'department_id': 4,
            'username': 'fuhaitian',
            'name': '傅海天',
        },
        {
            'department_id': 4,
            'username': 'fupengsong',
            'name': '傅朋松',
        },
        {
            'department_id': 4,
            'username': 'huhongdi',
            'name': '胡红狄',
        },
        {
            'department_id': 4,
            'username': 'lizhiwen',
            'name': '李志文',
        },
        {
            'department_id': 4,
            'username': 'maojiafeng',
            'name': '毛佳峰',
        },
        {
            'department_id': 4,
            'username': 'renhualiang',
            'name': '任华梁',
        },
        {
            'department_id': 4,
            'username': 'sunbo',
            'name': '孙波',
        },
        {
            'department_id': 4,
            'username': 'sunqi',
            'name': '孙琦',
        },
        {
            'department_id': 4,
            'username': 'wangjianan',
            'name': '王佳楠',
        },
        {
            'department_id': 4,
            'username': 'wangxin',
            'name': '王新',
        },
        {
            'department_id': 4,
            'username': 'wuhu',
            'name': '吴虎',
        },
        {
            'department_id': 4,
            'username': 'wuwenwei',
            'name': '吴文威',
        },
        {
            'department_id': 4,
            'username': 'xiejing',
            'name': '谢晶',
        },
        {
            'department_id': 4,
            'username': 'yuyang',
            'name': '俞洋',
        },
        {
            'department_id': 4,
            'username': 'zhangyixin',
            'name': '张译心',
        },
        {
            'department_id': 4,
            'username': 'zhengzhi',
            'name': '郑植',
        },
        {
            'department_id': 4,
            'username': 'zhouhao',
            'name': '周昊',
        },
        {
            'department_id': 4,
            'username': 'zhouzenghua',
            'name': '周增华',
        },

        # 财务审计部
        {
            'department_id': 5,
            'username': 'qihuizhen',
            'name': '祁辉真',
        },
        {
            'department_id': 5,
            'username': 'zhanghuanjun',
            'name': '张焕军',
        },
        {
            'department_id': 5,
            'username': 'wujie',
            'name': '吴婕',
        },
        {
            'department_id': 5,
            'username': 'lizhenfei',
            'name': '李珍飞',
        },
        {
            'department_id': 5,
            'username': 'qianjing',
            'name': '钱璟',
        },
        {
            'department_id': 5,
            'username': 'wangjianbin',
            'name': '王建斌',
        },
        {
            'department_id': 5,
            'username': 'xiangyuting',
            'name': '项宇婷',
        },
        {
            'department_id': 5,
            'username': 'xuzhiwen',
            'name': '徐芷文',
        },
        {
            'department_id': 5,
            'username': 'yukejie',
            'name': '俞科杰',
        },
        {
            'department_id': 5,
            'username': 'zhuyanjun',
            'name': '朱艳君',
        },

        # 资产经营事业部
        {
            'department_id': 6,
            'username': 'panjunxing',
            'name': '潘俊行',
        },
        {
            'department_id': 6,
            'username': 'daiyiyi',
            'name': '戴毅毅',
        },
        {
            'department_id': 6,
            'username': 'hanyu',
            'name': '韩煜',
        },
        {
            'department_id': 6,
            'username': 'yanmiaofu',
            'name': '颜妙富',
        },
    ]

    def handle(self, *args, **options):
        for user in self.users:
            create_user(
                user['username'],
                user['name'],
                user['department_id']
            )
        self.stdout.write('Successfully created user')
