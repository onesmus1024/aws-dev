
import boto3



class IAM:
    
        def __init__(self):
            self.iam = boto3.client('iam')
            self.available_users = self._get_all_users_names()
            self.available_groups = self._get_all_groups_names()
            self.available_policies = self._get_all_policies_names()
            self.available_roles = self._get_all_roles_names()
        
        
        # get all iam users
        def _get_all_users_names(self):
            return [user['UserName'] for user in self.iam.list_users()['Users']]
        
        def _get_all_groups_names(self):
            return [group['GroupName'] for group in self.iam.list_groups()['Groups']]
        
        def _get_all_policies_names(self):
            return [policy['PolicyName'] for policy in self.iam.list_policies()['Policies']]
        
        def _get_all_roles_names(self):
            return [role['RoleName'] for role in self.iam.list_roles()['Roles']]
        

        
        # create iam user
        def create_user(self, user_name):
            try:
                if user_name in self.available_users:
                    print('User already exists')
                    return
                self.iam.create_user(UserName=user_name)
            except Exception as e:
                raise e
    
    
        # delete iam user
        def delete_user(self, user_name):
            try:
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                self.iam.delete_user(UserName=user_name)
            except Exception as e:
                raise e
    
        # list iam users
        def list_users(self):
            try:
                for user in self.iam.list_users()['Users']:
                    print("User Name: {0}".format(user['UserName']))
                    print("User ID: {0}".format(user['UserId']))
                    print("User ARN: {0}".format(user['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
        
        # create iam group
        def create_group(self, group_name):
            try:
                if group_name in self.available_groups:
                    print('Group already exists')
                    return
                self.iam.create_group(GroupName=group_name)
            except Exception as e:
                raise e
            
        # delete iam group
        def delete_group(self, group_name):
            try:
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                self.iam.delete_group(GroupName=group_name)
            except Exception as e:
                raise e
            
        # list iam groups
        def list_groups(self):
            try:
                for group in self.iam.list_groups()['Groups']:
                    print("Group Name: {0}".format(group['GroupName']))
                    print("Group ID: {0}".format(group['GroupId']))
                    print("Group ARN: {0}".format(group['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            

        # create iam policy 
        def create_policy(self, policy_name, policy_document):
            try:
                if policy_name in self.available_policies:
                    print('Policy already exists')
                    return
                self.iam.create_policy(PolicyName=policy_name, PolicyDocument=policy_document)
            except Exception as e:
                raise e
            

        # delete iam policy
        def delete_policy(self, policy_name):
            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                self.iam.delete_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'])
            except Exception as e:
                raise e
            

        # list iam policies
        def list_policies(self):
            try:
                for policy in self.iam.list_policies()['Policies']:
                    print("Policy Name: {0}".format(policy['PolicyName']))
                    print("Policy ID: {0}".format(policy['PolicyId']))
                    print("Policy ARN: {0}".format(policy['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            

        # create iam role
        def create_role(self, role_name, assume_role_policy_document):
            try:
                if role_name in self.available_roles:
                    print('Role already exists')
                    return
                self.iam.create_role(RoleName=role_name, AssumeRolePolicyDocument=assume_role_policy_document)
            except Exception as e:
                raise e
            

        # delete iam role
        def delete_role(self, role_name):
            try:
                if role_name not in self.available_roles:
                    print('Role does not exist')
                    return
                self.iam.delete_role(RoleName=role_name)
            except Exception as e:
                raise e
            
        # list iam roles
        def list_roles(self):
            try:
                for role in self.iam.list_roles()['Roles']:
                    print("Role Name: {0}".format(role['RoleName']))
                    print("Role ID: {0}".format(role['RoleId']))
                    print("Role ARN: {0}".format(role['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            
        # attach iam policy to iam user
        def attach_policy_to_user(self, policy_name, user_name):
            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                self.iam.attach_user_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], UserName=user_name)
            except Exception as e:
                raise e
            

        # attach iam policy to iam group
        def attach_policy_to_group(self, policy_name, group_name):

            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                self.iam.attach_group_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], GroupName=group_name)
            except Exception as e:
                raise e
            

        # attach iam policy to iam role
        def attach_policy_to_role(self, policy_name, role_name):
            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if role_name not in self.available_roles:
                    print('Role does not exist')
                    return
                self.iam.attach_role_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], RoleName=role_name)
            except Exception as e:
                raise e
            
        # detach iam policy from iam user
        def detach_policy_from_user(self, policy_name, user_name):
            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                self.iam.detach_user_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], UserName=user_name)
            except Exception as e:
                raise e
            

        # detach iam policy from iam group
        def detach_policy_from_group(self, policy_name, group_name):
            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                self.iam.detach_group_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], GroupName=group_name)
            except Exception as e:
                raise e
            
        # detach iam policy from iam role
        def detach_policy_from_role(self, policy_name, role_name):

            try:
                if policy_name not in self.available_policies:
                    print('Policy does not exist')
                    return
                if role_name not in self.available_roles:
                    print('Role does not exist')
                    return
                self.iam.detach_role_policy(PolicyArn=self.iam.get_policy(PolicyArn=policy_name)['Policy']['Arn'], RoleName=role_name)
            except Exception as e:
                raise e
            
        # add iam user to iam group
        def add_user_to_group(self, user_name, group_name):
            try:
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                self.iam.add_user_to_group(UserName=user_name, GroupName=group_name)
            except Exception as e:
                raise e
            
        # remove iam user from iam group
        def remove_user_from_group(self, user_name, group_name):
            try:
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                self.iam.remove_user_from_group(UserName=user_name, GroupName=group_name)
            except Exception as e:
                raise e
            
        # list iam users
        def list_users(self):
            try:
                for user in self.iam.list_users()['Users']:
                    print("User Name: {0}".format(user['UserName']))
                    print("User ID: {0}".format(user['UserId']))
                    print("User ARN: {0}".format(user['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            
        # list iam groups
        def list_groups(self):
            try:
                for group in self.iam.list_groups()['Groups']:
                    print("Group Name: {0}".format(group['GroupName']))
                    print("Group ID: {0}".format(group['GroupId']))
                    print("Group ARN: {0}".format(group['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            

        # list iam policies
        def list_policies(self):
            try:
                for policy in self.iam.list_policies()['Policies']:
                    print("Policy Name: {0}".format(policy['PolicyName']))
                    print("Policy ID: {0}".format(policy['PolicyId']))
                    print("Policy ARN: {0}".format(policy['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            

        # list iam roles
        def list_roles(self):
            try:
                for role in self.iam.list_roles()['Roles']:
                    print("Role Name: {0}".format(role['RoleName']))
                    print("Role ID: {0}".format(role['RoleId']))
                    print("Role ARN: {0}".format(role['Arn']))
                    print("="*50)
            except Exception as e:
                raise e
            

        # list iam policies attached to iam user
        def list_user_policies(self, user_name):
            try:
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                for policy in self.iam.list_user_policies(UserName=user_name)['PolicyNames']:
                    print("Policy Name: {0}".format(policy))
                    print("="*50)
            except Exception as e:
                raise e
            
        # list iam policies attached to iam group
        def list_group_policies(self, group_name):
            try:
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                for policy in self.iam.list_group_policies(GroupName=group_name)['PolicyNames']:
                    print("Policy Name: {0}".format(policy))
                    print("="*50)
            except Exception as e:
                raise e
            

        # list iam policies attached to iam role
        def list_role_policies(self, role_name):

            try:
                if role_name not in self.available_roles:
                    print('Role does not exist')
                    return
                for policy in self.iam.list_role_policies(RoleName=role_name)['PolicyNames']:
                    print("Policy Name: {0}".format(policy))
                    print("="*50)
            except Exception as e:
                raise e
            
        # list iam groups attached to iam user
        def list_user_groups(self, user_name):
            try:
                if user_name not in self.available_users:
                    print('User does not exist')
                    return
                for group in self.iam.list_groups_for_user(UserName=user_name)['Groups']:
                    print("Group Name: {0}".format(group['GroupName']))
                    print("="*50)
            except Exception as e:
                raise e
            
        # list iam users attached to iam group
        def list_group_users(self, group_name):
            try:
                if group_name not in self.available_groups:
                    print('Group does not exist')
                    return
                for user in self.iam.get_group(GroupName=group_name)['Users']:
                    print("User Name: {0}".format(user['UserName']))
                    print("="*50)
            except Exception as e:
                raise e
            
        # list iam policies attached to iam role
        def list_role_policies(self, role_name):
                
                try:
                    if role_name not in self.available_roles:
                        print('Role does not exist')
                        return
                    for policy in self.iam.list_role_policies(RoleName=role_name)['PolicyNames']:
                        print("Policy Name: {0}".format(policy))
                        print("="*50)
                except Exception as e:
                    raise e
                







if __name__ == '__main__':

    iam = IAM()

    # list iam users
    iam.list_users()
            