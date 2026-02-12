package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c1892b99d38073cd53c44cdf0fc473ede529188d424468bf90ec2c0ff93eca91_flash_display_Sprite extends Sprite
   {
       
      
      public function _c1892b99d38073cd53c44cdf0fc473ede529188d424468bf90ec2c0ff93eca91_flash_display_Sprite()
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
