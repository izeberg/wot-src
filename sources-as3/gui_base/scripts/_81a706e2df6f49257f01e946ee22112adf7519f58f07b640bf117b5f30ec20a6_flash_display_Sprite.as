package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _81a706e2df6f49257f01e946ee22112adf7519f58f07b640bf117b5f30ec20a6_flash_display_Sprite extends Sprite
   {
       
      
      public function _81a706e2df6f49257f01e946ee22112adf7519f58f07b640bf117b5f30ec20a6_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
