from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import MyTokenObtainPairSerializer, ResetPasswordSerailizer, SetNewPasswordSerailizer, UserCreationSerializer
from .models import User



# password reset token geneator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 

# send mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util


class AuthenticationUser(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello"},status=status.HTTP_200_OK)


class CreateUser(generics.CreateAPIView):
    # first data comes here
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    permission_classes=(AllowAny,)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class TokenGeneratorEmailView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerailizer
    def post(self,request):
        data = {'request':request,'data':request.data}
        serializer = self.serializer_class(data=data)
        print("My serializer")
        print(serializer)
        email = request.data['email']
        print(email)
        # after that is goes to sertializer and if it works.
        if User.objects.filter(email=email).exists():
                #getting username as email
                user = User.objects.get(email=email)
                print(user.id)
                print("*********************************************")
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                # generating token
                
                token = PasswordResetTokenGenerator().make_token(user)
                # getting current domain or site
                current_site = get_current_site(request=request).domain
                relativeLink = reverse('password-change',kwargs={'uidb64':uidb64,'token':token}) 

                print("stha.binod1000@gmail.com")

                absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
                email_body = 'Hi'+user.email+', use this link to reset password '+absurl
                data = {'email_body':email_body,'to_email':user.email,'email_subject':'Welcome to TLMS, please change your password.'}
                Util.send_email(data)
            # validation working
                return Response({"Success":"You are invited for TMLS as role please change your password!"},status=status.HTTP_200_OK)
        return Response({"error":"Email address not found!"},status=status.HTTP_200_OK)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self,request,uidb64,token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({"error":"Token is not valid, please request a new one"},status=status.HTTP_401_UNAUTHORIZED)
            return Response({"success":True,'message':'credentials valid','uidb64':uidb64,'token':token},status=status.HTTP_200_OK)

            
        except DjangoUnicodeDecodeError:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({"error":"Token is not valid, please request a new one"},status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerailizer

    def patch(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True,'message':"Password reset success"},status=status.HTTP_200_OK)


