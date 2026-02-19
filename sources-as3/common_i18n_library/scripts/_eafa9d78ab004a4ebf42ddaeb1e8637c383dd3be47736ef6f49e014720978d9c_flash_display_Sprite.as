package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _eafa9d78ab004a4ebf42ddaeb1e8637c383dd3be47736ef6f49e014720978d9c_flash_display_Sprite extends Sprite
   {
       
      
      public function _eafa9d78ab004a4ebf42ddaeb1e8637c383dd3be47736ef6f49e014720978d9c_flash_display_Sprite()
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
