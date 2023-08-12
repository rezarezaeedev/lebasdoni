from rest_access_policy import AccessPolicy


class ProductInfoAccessPolicy(AccessPolicy):
    statements = [
    	{
    		'action':['*'],
    		'principal':'group:SuperUser',
    		'effect':'allow'
    	},
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update", 'destroy'],
            "principal": ["group:SellerUser"],
            "effect": "allow"
        }
    ]


class ProductAccessPolicy(AccessPolicy):
    statements = [
    	{
    		'action':['*'],
    		'principal':'group:SuperUser',
    		'effect':'allow'
    	},
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update", 'destroy'],
            "principal": ["group:SellerUser"],
            "effect": "allow"
        }
    ]


class CategoryAccessPolicy(AccessPolicy):
    statements = [
    	{
    		'action':['*'],
    		'principal':'group:SuperUser',
    		'effect':'allow'
    	},
    	{
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["list", "retrieve", "update", "partial_update", 'destroy'],
            "principal": ["group:AdminUser"],
            "effect": "allow"
        }
    ]


class LikeAndCommentAccessPolicy(AccessPolicy):
    statements = [
    	{
    		'action':['*'],
    		'principal':'group:SuperUser',
    		'effect':'allow'
    	},
        {
            "action": ['<method:post>', '<method:put>', '<method:patch>', '<method:delete>',],
            "principal": ["group:CustomerUser"],
            "effect": "allow"
        }
    ]


