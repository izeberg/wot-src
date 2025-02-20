package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _913242d99a54a64b0ac2afe8aab7ad3ed40c1ec2b5224ba50c254293fc100047_flash_display_Sprite extends Sprite
   {
       
      
      public function _913242d99a54a64b0ac2afe8aab7ad3ed40c1ec2b5224ba50c254293fc100047_flash_display_Sprite()
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
